class Triangle
    attr_reader :a, :b, :c

    def initialize(a,b,c)
        @a = a
        @b = b
        @c = c
    end

    def kind
        raise ArgumentError if invalid
        return 'equilateral' if a == b && b == c
        return 'isosceles' if a == b || b == c || c == a
        'equilateral'
    end

    private

    def invalid
        return true if a <= 0 || b <= 0 || c <= 0
        return true if a + b <= c || b + c <= a || c + a <= b
        false
    end
end