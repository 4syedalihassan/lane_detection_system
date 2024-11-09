import cProfile
import pstats
from io import StringIO

def profile_function(func, *args, **kwargs):
    profiler = cProfile.Profile()
    profiler.enable()
    func(*args, **kwargs)
    profiler.disable()
    
    s = StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())
