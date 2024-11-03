# class Banner
#     def initialize(message)
#         @message = message
#     end

#     def to_s
#         [horizontal_rule, empty_line, message_line, empty_line, horizontal_rule].join("\n")
#     end

#     private

#     def horizontal_rule
#         "+-#{'-' * @message.length()}-+"
#     end

#     def empty_line
#         "| #{' ' * @message.length()} |"
#     end

#     def message_line
#         "| #{@message} |"
#     end
# end

# banner = Banner.new('To boldly go where no one has gone before.')
# puts banner

# banner = Banner.new('')
# puts banner

# puts "What's the Output?"

# class Pet
#     attr_reader :name

#     def initialize(name)
#         @name = name.to_s
#     end

#     def to_s
#         @name.upcase!
#         "My name is #{@name}."
#     end
# end

# name = 'Fluffy'
# fluffy = Pet.new(name)
# puts fluffy.name
# puts fluffy
# puts fluffy.name
# puts name



# puts "Fix the Program - Books (Part 1)"

# class Book
#     attr_reader :author, :title

#     def initialize(author, title)
#         @author = author
#         @title = title
#     end

#     def to_s
#         %("#{title}", by #{author})
#     end
# end

# book = Book.new("Neil Stephenson", "Snow Crash")
# puts %(The author of "#{book.title}" is #{book.author}.)
# puts %(book = #{book}.)

# # The author of "Snow Crash" is Neil Stephenson.
# # book = "Snow Crash", by Neil Stephenson.



puts "Fix the Program - Books (Part 2)"

class Book
    attr_accessor :author, :title

    def to_s
        %("#{title}", by #{author})
    end
end

book = Book.new
book.author = "Neil Stephenson"
book.title = "Snow Crash"
puts %(The author of "#{book.title}" is #{book.author}.)
puts %(book = #{book}.)

# The author of "Snow Crash" is Neil Stephenson.
# book = "Snow Crash", by Neil Stephenson.

puts "Fix the Program - Persons"

class Person
    attr_writer :first_name, :last_name

    def initialize(first_name, last_name)
        @first_name = first_name.capitalize
        @last_name = last_name.capitalize
    end

    def to_s
        "#{@first_name} #{@last_name}"
    end
end

person = Person.new('john', 'doe')
puts person

person.first_name = 'jane'
person.last_name = 'smith'
puts person

puts "Fix the Program - Flight Data"

class Flight
    attr_accessor :database_handle

    def initialize(flight_number)
        @database_handle = Database.init
        @flight_number = flight_number
    end
end


puts "Buggy Code - Car Mileage"


class Car
    attr_accessor :mileage

    def initialize
        @mileage = 0
    end

    def increment_mileage(miles)
        self.mileage += miles
    end

    def print_mileage
        puts mileage
    end
end

car = Car.new
car.mileage = 5000
car.increment_mileage(678)
car.print_mileage  # should print 5678


puts "Rectangles and Squares"

class Rectangle
    def initialize(height, width)
        @height = height
        @width = width
    end

    def area
        @height * @width
    end
end

class Square < Rectangle
    def initialize(length)
        @height = length
        @width = length
    end
end

square = Square.new(5)
puts "area of square = #{square.area}"