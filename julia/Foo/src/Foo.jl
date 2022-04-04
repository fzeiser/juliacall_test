module Foo
export foo

using PythonCall

function foo(a)
	println(typeof(a))
	b = pyconvert(Array, a)
	println(typeof(b))
end

end
