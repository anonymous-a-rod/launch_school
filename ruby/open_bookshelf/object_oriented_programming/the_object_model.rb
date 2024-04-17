# exercise 1

# everything stored in memory in ruby is an object

# exercise 2

module Celebrate
  def celebrate
    puts "Merry Christmas"
  end
end

class Christmas
  include Celebrate
end

holiday = Christmas.new

holiday.celebrate

# module allows you to "mixin" common blocks on code into multiple classes. Write include followed by the name.