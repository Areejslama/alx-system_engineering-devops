#!/usr/bin/env ruby
input_string = ARGV[0]
regex_pattern = /\[(.*?),(.*?),(.*?)\]/
matches = input_string.match(regex_pattern)
if matches
  sender = matches[1]
  receiver = matches[2]
  flags = matches[3]

  puts "Sender: #{sender}"
  puts "Receiver: #{receiver}"
  puts "Flags: #{flags}"
else
  puts "Invalid input format"
end
