module Bar
export bar

# using PythonCall

function bar(a)
	println(typeof(a))
	# b = pyconvert(Array, a)
	# println(typeof(b))
end

end
