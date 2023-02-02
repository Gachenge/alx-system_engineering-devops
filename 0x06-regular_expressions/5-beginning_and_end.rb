#!/usr/bin/env ruby
#starts with h ends with n, anything in between

puts ARGV[0].scan(/^h.n$/).join
