def dms(num)
    d = num.floor
    minutes_per_degree = 1.0 / 60.0
    m = ((num % 1) / minutes_per_degree).floor
    seconds_per_degree = minutes_per_degree / 60.0
    s = ((num % minutes_per_degree) / seconds_per_degree).round
    m += (s / 60)
    s %= 60

    d %= 360
    m = "0#{m}" if m < 10 
    s = "0#{s}" if s < 10

    %(#{d}°#{m}'#{s}")
end

# All test cases should return true
                %(30°00'00")
puts dms(30) == %(30°00'00")
puts dms(76.73) == %(76°43'48")
puts dms(254.6) == %(254°36'00")
puts dms(93.034773) == %(93°02'05")
puts dms(0) == %(0°00'00")
puts dms(360) == %(360°00'00") || dms(360) == %(0°00'00")