def missing_digit(str)
  a, operator, b, _, c = str.split(' ')
  (0..9).each do |int|
    int = int.to_s
    x, y, z = a.gsub('x', int).to_i, b.gsub('x', int).to_i, c.gsub('x', int).to_i
    case operator
    when '+'
      return int if x + y == z
    when '-'
      return int if x - y == z
    when '*'
      return int if x * y == z
    when '/'
      return int if x / y == z
    end
  end
  return -1
end


p missing_digit('2 + 6 = x')
p missing_digit('2x - 14 = 6')
p missing_digit('1x / 6 = 2')
p missing_digit('3 * 6 = 1x')