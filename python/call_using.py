from juliacall import Main as jl
import os

julia_dir = os.getcwd() + "/../julia"

# jl.seval('push!(LOAD_PATH, f"{julia_dir}/Foo/src")')
jl.seval(f'import Pkg; Pkg.develop(path="{julia_dir}/Foo")')
jl.seval("using Foo")

print(jl.foo([1, 2, 3]))
