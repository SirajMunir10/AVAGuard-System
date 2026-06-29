# Python 3.14+ compatibility patch for Django Context copying
# Ref: https://github.com/django/django/commit/08b5e28a
try:
    from django.template.context import BaseContext
    import copy

    # Test if copy(super()) fails in this environment
    try:
        ctx = BaseContext()
        copy.copy(ctx)
    except AttributeError:
        # Patch BaseContext.__copy__ to avoid copy(super())
        def patched_copy(self):
            duplicate = self.__class__.__new__(self.__class__)
            duplicate.__dict__.update(self.__dict__)
            duplicate.dicts = self.dicts[:]
            return duplicate

        BaseContext.__copy__ = patched_copy
except ImportError:
    pass
