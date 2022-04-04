from juliacall import Main as jl
import os

julia_dir = os.getcwd() + "/../julia"
jl.seval(f'include("{julia_dir}/Foo/src/Foo.jl")')

print(jl.Foo.foo([1, 2, 3]))
