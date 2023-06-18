__all__ = ["__version__", "version_tuple"]

try:
    from ._version import version as __version__, version_tuple
except ImportError:
    __version__ = "unknown"
    version_tuple = (0, 0, "unknown")