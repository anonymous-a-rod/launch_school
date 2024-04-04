# def short_long_short(string_a, string_b) 
#     length_a = string_a.length
#     length_b = string_b.length
#     shorter = length_a > length_b ? string_b : string_a
#     longer = length_a > length_b ? string_a : string_b

#     shorter + longer + shorter
# end

# puts short_long_short('abc', 'defgh') == "abcdefghabc"
# puts short_long_short('abcde', 'fgh') == "fghabcdefgh"
# puts short_long_short('', 'xyz') == "xyz"

# def century(year)
#     century = ((year - 1) / 100) + 1
    
#     last_two_digits =  century % 100

#     return "#{century}th" if last_two_digits == 11 || last_two_digits == 12 || last_two_digits == 13

#     last_int =  century % 10
    
#     case last_int
#     when 1 then return "#{century}st"
#     when 2 then return "#{century}nd"
#     when 3 then return "#{century}rd"
#     else        return "#{century}th"
#     end
# end

# puts century(2000) == '20th'
# puts century(2001) == '21st'
# puts century(1965) == '20th'
# puts century(256) == '3rd'
# puts century(5) == '1st'
# puts century(10103) == '102nd'
# puts century(1052) == '11th'
# puts century(1127) == '12th'
# puts century(11201) == '113th'

# def leap_year?(year)
#     multiple_of_4 = year % 4 == 0
#     multiple_of_100 = year % 100 == 0
#     multiple_of_400 = year % 400 == 0
    
#     return false unless multiple_of_4
#     if year > 1752 
#         return false if multiple_of_100 && !multiple_of_400
#     end
#     true
# end

# puts leap_year?(2016) == true
# puts leap_year?(2015) == false
# puts leap_year?(2100) == false
# puts leap_year?(2400) == true
# puts leap_year?(240000) == true
# puts leap_year?(240001) == false
# puts leap_year?(2000) == true
# puts leap_year?(1900) == false
# puts leap_year?(1752) == true
# puts leap_year?(1700) == true
# puts leap_year?(1) == false
# puts leap_year?(100) == true
# puts leap_year?(400) == true

# def multisum(n)
#     array = []
#     [*1..n].each do |x|
#         array << x if x % 3 == 0 || x % 5 == 0
#     end
#     array.sum
# end

# puts multisum(3) == 3
# puts multisum(5) == 8
# puts multisum(10) == 33
# puts multisum(1000) == 234168

# def running_total(array)
#     running_total = []

#     array.each_with_index do |_, i|
#         running_total << (array.slice(0, i+1)).sum
#     end

#     running_total
# end

# puts running_total([2, 5, 13]) == [2, 7, 20]
# puts running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67]
# puts running_total([3]) == [3]
# puts running_total([]) == []


# def string_to_signed_integer(string)
#     negative = string[0] == '-'
#     if negative || string[0] == '+'
#         string = string.split('').slice(1..-1).join('')
#     end

#     convert = {
#         '0' => 0,
#         '1' => 1,
#         '2' => 2,
#         '3' => 3,
#         '4' => 4,
#         '5' => 5,
#         '6' => 6,
#         '7' => 7,
#         '8' => 8,
#         '9' => 9
#     }

#     num = 0

#     string.split('').reverse.each_with_index do |element, index|
#         num += (convert[element] * (10 ** index))
#     end

#     num *= -1 if negative
#     num
# end

# puts string_to_signed_integer('4321') == 4321
# puts string_to_signed_integer('-570') == -570
# puts string_to_signed_integer('+100') == 100

def signed_integer_to_string(num)
    convert = {
        0 => '0',
        1 => '1',
        2 => '2',
        3 => '3',
        4 => '4',
        5 => '5',
        6 => '6',
        7 => '7',
        8 => '8',
        9 => '9'
    }

    string = ''

    return '0' if num == 0
    negative = num < 0
    num *= -1 if negative

    while num > 0
        string = convert[num % 10] + string
        num = (num / 10).floor
    end
    sign = negative ? "-" : "+"
    sign + string
end


puts signed_integer_to_string(4321) == '+4321'
puts signed_integer_to_string(-123) == '-123'
puts signed_integer_to_string(0) == '0'