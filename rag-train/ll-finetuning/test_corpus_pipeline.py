#!/usr/bin/env python3
"""
Unit tests for the AVAGuard corpus pipeline.

Tests score_entry() and detect_off_topic() from corpus_audit.py with cases
covering all scoring branches and off-topic detection patterns.

Run:
    python -m pytest test_corpus_pipeline.py -v
    python test_corpus_pipeline.py
"""

import sys
import unittest
from pathlib import Path

# Bootstrap: add scripts directory to path so imports work from project root
SCRIPTS_DIR = Path(__file__).resolve().parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from corpus_audit import score_entry, detect_off_topic, OFF_TOPIC_KEYWORDS  # noqa: E402


# ── Fixtures ───────────────────────────────────────────────────────────────────

def _complete_entry() -> dict:
    """A fully-populated entry that should score 10/10."""
    return {
        "id": "autopilot-esp-001",
        "domain": "Intune",
        "subdomain": "Autopilot",
        "incident_type": "Troubleshooting",
        "query": "Autopilot ESP is stuck at 'Preparing your device for mobile management' for 45 minutes",
        "environment_context": {
            "tenant_type": "Commercial M365",
            "mdm_authority": "Intune standalone",
        },
        "symptoms": [
            "Enrollment Status Page (ESP) remains on 'Preparing your device' phase",
            "Device shows as 'Not compliant' in Intune portal during ESP",
        ],
        "error_codes": ["0x800705B4", "0x81036502"],
        "root_causes": [
            "Required app assigned to user group instead of device group during ESP",
        ],
        "remediation_steps": [
            "In MEM portal, change required app assignment target from user group to device group",
            "Verify Autopilot profile is assigned to the correct device group",
            "Reset device and re-enroll to trigger a clean ESP pass",
        ],
        "validation": "Confirm ESP completes within the configured timeout (default 60 minutes)",
        "rollback": "Reset the device using Windows Recovery; remove from Autopilot device list",
        "source_references": [
            "https://learn.microsoft.com/en-us/mem/autopilot/troubleshoot-oobe"
        ],
        "provenance": "Extracted from: https://learn.microsoft.com/en-us/mem/autopilot/troubleshoot-oobe",
        "generation_method": "extracted",
    }


def _titles_only_entry() -> dict:
    """An entry with only title/query and no operational depth — should score 0–2."""
    return {
        "id": "autopilot-titles-001",
        "domain": "Intune",
        "subdomain": "Autopilot",
        "incident_type": "Troubleshooting",
        "query": "Troubleshooting Autopilot Enrollment Status Page timeout errors",
    }


def _htb_entry() -> dict:
    """A HackTheBox penetration testing entry — should be flagged off-topic."""
    return {
        "instruction": "How do you perform an initial port scan on a HackTheBox target?",
        "input": "Target IP: 10.10.11.80. No prior knowledge.",
        "output": (
            "Command: `nmap -p- --min-rate 10000 -sV 10.10.11.80`\n"
            "Explanation: Scans all 65535 ports at high speed. Identify open services.\n"
            "Then use evil-winrm or netcat depending on the service found."
        ),
        "source": "HackTheBox — Machine: Forest",
    }


def _entry_without_error_codes() -> dict:
    """An entry with most fields but no error_codes — should score 5–6.

    Fields present: source_references (+2), remediation_steps (+2),
    symptoms (+1), environment_context (+1) = 6 max without error_codes.
    error_codes is absent, so the 2-point error_codes score is not earned.
    validation and rollback are also absent to keep score at 6 (not 8).
    """
    return {
        "source_references": ["https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access"],
        "error_codes": [],  # deliberately empty — this is the field under test
        "remediation_steps": [
            "Review sign-in logs in Entra ID for the blocked user",
            "Check Named Locations to confirm IP range is correctly defined",
        ],
        "symptoms": ["User cannot sign in, receives 'Your sign-in was blocked' message"],
        "environment_context": {"tenant_type": "Hybrid", "relevant_config": "CA policy targeting All users"},
        # validation and rollback intentionally omitted to keep total at 6
    }


def _microsoft_cloud_entry() -> dict:
    """A legitimate Microsoft cloud operational entry — should NOT be flagged off-topic."""
    return {
        "domain": "Entra ID",
        "subdomain": "Conditional Access",
        "incident_type": "Troubleshooting",
        "query": "Conditional Access policy is blocking MFA-exempt service accounts",
        "symptoms": ["Service account sign-ins blocked by CA policy targeting all users"],
        "error_codes": ["AADSTS53003"],
        "remediation_steps": [
            "Create an exclusion group for service accounts in the CA policy",
            "Add service account UPNs to the exclusion group",
        ],
        "source_references": [
            "https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access"
        ],
    }


# ── Test: score_entry() ────────────────────────────────────────────────────────

class TestScoreEntry(unittest.TestCase):
    """Tests for score_entry() — 0–10 completeness scoring."""

    def test_complete_entry_scores_10(self):
        """A fully populated entry with all 7 fields should score 10."""
        entry = _complete_entry()
        self.assertEqual(score_entry(entry), 10, "Complete entry should score 10/10")

    def test_titles_only_entry_scores_0_to_2(self):
        """An entry with only a query and metadata should score 0–2."""
        entry = _titles_only_entry()
        score = score_entry(entry)
        self.assertLessEqual(score, 2, f"Titles-only entry should score ≤ 2, got {score}")

    def test_missing_source_references_loses_2_points(self):
        """Removing source_references from a complete entry should cost exactly 2 points."""
        full = _complete_entry()
        no_refs = {k: v for k, v in full.items() if k != "source_references"}
        self.assertEqual(score_entry(full) - score_entry(no_refs), 2)

    def test_missing_error_codes_loses_2_points(self):
        """Removing error_codes from a complete entry should cost exactly 2 points."""
        full = _complete_entry()
        no_codes = {k: v for k, v in full.items() if k != "error_codes"}
        self.assertEqual(score_entry(full) - score_entry(no_codes), 2)

    def test_partial_entry_missing_error_codes_scores_5_to_6(self):
        """Entry with all fields except error_codes should score 5–6."""
        entry = _entry_without_error_codes()
        score = score_entry(entry)
        self.assertGreaterEqual(score, 5, f"Expected score ≥ 5, got {score}")
        self.assertLessEqual(score, 6, f"Expected score ≤ 6, got {score}")

    def test_single_remediation_step_does_not_earn_points(self):
        """A single remediation step does not meet the ≥2 requirement — 0 points."""
        entry = {"remediation_steps": ["Only one step — this should not score"]}
        self.assertEqual(score_entry(entry), 0,
                         "Single step should NOT earn remediation points")

    def test_two_remediation_steps_earns_2_points(self):
        """Exactly 2 remediation steps should earn the 2-point remediation score."""
        entry = {"remediation_steps": ["Step one", "Step two"]}
        self.assertEqual(score_entry(entry), 2)

    def test_empty_source_references_list_scores_0(self):
        """An empty source_references list should not earn the 2-point reference score."""
        entry = {"source_references": []}
        self.assertEqual(score_entry(entry), 0)

    def test_whitespace_only_source_reference_scores_0(self):
        """A source_references list containing only whitespace strings should score 0."""
        entry = {"source_references": ["   ", "\t"]}
        self.assertEqual(score_entry(entry), 0)

    def test_empty_error_codes_list_scores_0(self):
        """An empty error_codes list should not earn the 2-point error code score."""
        entry = {"error_codes": []}
        self.assertEqual(score_entry(entry), 0)

    def test_whitespace_only_validation_does_not_score(self):
        """A validation field containing only whitespace should not score."""
        entry = {"validation": "   "}
        self.assertEqual(score_entry(entry), 0)

    def test_empty_entry_scores_0(self):
        """A completely empty dict should score 0."""
        self.assertEqual(score_entry({}), 0)

    def test_environment_context_with_empty_values_does_not_score(self):
        """An environment_context dict with all empty values should not score."""
        entry = {"environment_context": {"tenant_type": "", "relevant_config": ""}}
        self.assertEqual(score_entry(entry), 0)

    def test_environment_context_with_one_value_scores(self):
        """An environment_context dict with at least one non-empty value should score."""
        entry = {"environment_context": {"tenant_type": "Commercial", "relevant_config": ""}}
        self.assertEqual(score_entry(entry), 1)

    def test_maximum_score_is_10(self):
        """Score should never exceed 10 regardless of entry richness."""
        entry = _complete_entry()
        # Add extra fields that are not in the scoring schema
        entry["extra_field"] = "this should not add points"
        entry["error_codes"].append("EXTRA_CODE")
        self.assertLessEqual(score_entry(entry), 10)


# ── Test: detect_off_topic() ───────────────────────────────────────────────────

class TestDetectOffTopic(unittest.TestCase):
    """Tests for detect_off_topic() — HTB/CTF content detection."""

    def test_htb_entry_flagged(self):
        """A HackTheBox entry should be detected as off-topic."""
        entry = _htb_entry()
        self.assertTrue(
            detect_off_topic(entry, OFF_TOPIC_KEYWORDS),
            "HTB entry should be flagged off-topic"
        )

    def test_microsoft_cloud_entry_not_flagged(self):
        """A legitimate Microsoft cloud operations entry should NOT be flagged."""
        entry = _microsoft_cloud_entry()
        self.assertFalse(
            detect_off_topic(entry, OFF_TOPIC_KEYWORDS),
            "Microsoft cloud operational entry should not be flagged off-topic"
        )

    def test_evil_winrm_flagged(self):
        """Entry containing 'evil-winrm' should be flagged off-topic."""
        entry = {
            "output": "Use evil-winrm -i dc01.target.htb -u administrator -H <ntlm_hash>"
        }
        self.assertTrue(detect_off_topic(entry, OFF_TOPIC_KEYWORDS))

    def test_mimikatz_flagged(self):
        """Entry containing 'mimikatz' should be flagged off-topic."""
        entry = {
            "description": "Use mimikatz to dump LSASS credentials from the compromised host"
        }
        self.assertTrue(detect_off_topic(entry, OFF_TOPIC_KEYWORDS))

    def test_ctf_flag_pattern_flagged(self):
        """Entry containing 'flag{' should be flagged off-topic (CTF flag format)."""
        entry = {"output": "Submit the root flag: flag{d3adb33f_l0l_y0u_g0t_pwn3d}"}
        self.assertTrue(detect_off_topic(entry, OFF_TOPIC_KEYWORDS))

    def test_kerberoasting_in_attack_context_flagged(self):
        """'kerberoasting' in attacker context should be flagged."""
        entry = {
            "instruction": "How do you perform Kerberoasting on a service account?",
            "output": "Run: impacket-GetUserSPNs -request domain.local/user:pass"
        }
        self.assertTrue(detect_off_topic(entry, OFF_TOPIC_KEYWORDS))

    def test_nmap_in_attacker_context_flagged(self):
        """Entry using nmap for initial recon should be flagged."""
        entry = {
            "output": "Command: nmap -p- --min-rate 10000 -sV 10.10.11.80"
        }
        self.assertTrue(detect_off_topic(entry, OFF_TOPIC_KEYWORDS))

    def test_htb_ip_range_flagged(self):
        """HTB IP range (10.10.10.x / 10.10.11.x) should be flagged."""
        entry = {"description": "Target machine IP is 10.10.11.123"}
        self.assertTrue(detect_off_topic(entry, OFF_TOPIC_KEYWORDS))

    def test_case_insensitive_detection(self):
        """Off-topic detection must be case-insensitive."""
        entry = {"description": "Using NMAP and MIMIKATZ on the target system"}
        self.assertTrue(detect_off_topic(entry, OFF_TOPIC_KEYWORDS))

    def test_htb_uppercase_flagged(self):
        """'HTB' in uppercase should be caught."""
        entry = {"source": "HTB — Machine: Forest"}
        self.assertTrue(detect_off_topic(entry, OFF_TOPIC_KEYWORDS))

    def test_empty_entry_not_flagged(self):
        """An empty entry has no text to match — should not be flagged."""
        self.assertFalse(detect_off_topic({}, OFF_TOPIC_KEYWORDS))

    def test_nested_fields_searched(self):
        """off-topic keywords inside nested lists and dicts should be detected."""
        entry = {
            "remediation_steps": [
                "First try standard approach",
                "If that fails, use metasploit to escalate privileges",
            ]
        }
        self.assertTrue(detect_off_topic(entry, OFF_TOPIC_KEYWORDS))

    def test_non_string_fields_handled_safely(self):
        """Non-string fields (int, None) should not cause exceptions."""
        entry = {
            "domain": "Intune",
            "completeness_score": 7,
            "symptoms": None,
            "error_codes": [0x80070005],
        }
        # Should not raise — just not off-topic
        result = detect_off_topic(entry, OFF_TOPIC_KEYWORDS)
        self.assertIsInstance(result, bool)

    def test_empty_keyword_list_never_flags(self):
        """An empty keyword list should never flag any entry."""
        self.assertFalse(detect_off_topic(_htb_entry(), []))


if __name__ == "__main__":
    unittest.main(verbosity=2)
