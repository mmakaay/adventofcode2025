p$<.sum{|b|s=b.strip;12.downto(1).map{|i|c=s[0..s.size-i].chars.max;s=s[s.index(c)+1..-1];c}.join.to_i}
