class MyCar
  attr_reader :model, :year
  attr_accessor :color, :engine_on, :speed

  def initialize(year, color, model)
    @year = year
    @color = color
    @model = model
    @speed = 0
    @engine_on = false
  end

  def speed_up
    return 'Turn engine on' unless engine_on

    @speed += 10
  end

  def brake
    return nil unless engine_on

    @speed -= 10 unless @speed <= 0
  end

  def turn_on
    return 'Engine already on' if @engine_on

    @engine_on = true
  end

  def turn_off
    return 'Engine already off' unless @engine_on

    @engine_on = false
  end

  def spray_paint(color)
    @color = color
  end
end

prius = MyCar.new(2000, 'white', 'Toyota')

puts prius.engine_on
prius.turn_on
puts prius.engine_on

prius.spray_paint("black")
puts prius.color


