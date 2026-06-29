def ai_mode_processor(request):
    """
    Injects the current user's AI mode (mock or ai) into all templates.
    """
    if hasattr(request, 'session'):
        return {'ai_mode': request.session.get('ai_mode', 'ai')}
    return {'ai_mode': 'ai'}
