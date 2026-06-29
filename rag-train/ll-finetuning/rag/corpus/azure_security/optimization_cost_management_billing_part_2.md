# Optimization: Cost Management + Billing

**Domain:** Azure
**Subdomain:** Cost Management + Billing
**Incident Type:** Optimization

## Scenario / Query
A subscription shows underutilized ExpressRoute circuits with low average bandwidth usage over the past 30 days. How can I identify and right-size these circuits to reduce costs while maintaining required capacity?

## Environment Context
- **Tenant Type:** Enterprise (EA or MCA)
- **Configuration:** ExpressRoute circuits with a bandwidth of 1 Gbps or higher, monitored via Azure Monitor metrics for at least 30 days

## Symptoms
- Monthly ExpressRoute charges are higher than expected
- Average bandwidth utilization is below 20% of provisioned capacity
- Azure Advisor cost recommendations indicate underutilized circuits

## Error Codes
N/A

## Root Causes
1. ExpressRoute circuit bandwidth was provisioned based on peak estimates that are no longer accurate
2. Lack of regular review of circuit utilization metrics
3. No automated scaling or downgrade process in place

## Remediation Steps
1. 1. Review ExpressRoute circuit metrics in Azure Monitor: navigate to the circuit resource, select 'Metrics', and add the metric 'BitsInPerSecond' and 'BitsOutPerSecond' with an aggregation of 'Average' over a 30-day period.
2. 2. Compare the average bandwidth utilization against the provisioned circuit speed (e.g., 1 Gbps). If utilization is consistently below 20%, consider downgrading to a lower SKU (e.g., from 1 Gbps to 200 Mbps).
3. 3. To change the circuit SKU, use the Azure portal: open the ExpressRoute circuit, select 'Configuration', and under 'Bandwidth', select a lower value. Note that changing the SKU may require a brief service interruption and must be coordinated with the connectivity provider.
4. 4. Alternatively, use Azure PowerShell: `Set-AzExpressRouteCircuit -Name <circuitName> -ResourceGroupName <rgName> -BandwidthInMbps <newBandwidth>` (see official documentation for exact parameters).
5. 5. After the change, monitor the circuit to ensure performance remains acceptable.

## Validation
Verify that the new bandwidth SKU is active by checking the 'Provisioning State' and 'Circuit Provisioning State' in the Azure portal. Confirm that the monthly cost reflected in Cost Management + Billing has decreased.

## Rollback
To revert to the original bandwidth, repeat the same steps and select the previous higher bandwidth value. Ensure the connectivity provider supports the higher speed.

## References
- <https://learn.microsoft.com/en-us/azure/expressroute/optimize-costs>
- <https://learn.microsoft.com/en-us/azure/expressroute/expressroute-howto-circuit-portal-resource-manager>
