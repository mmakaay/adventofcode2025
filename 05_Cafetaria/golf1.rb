a,b=$<.read.split"\n\n"
p b.split.count{|i|i=i.to_i;a.split.any?{|s|m=s.split ?-;i>=m[0].to_i&&i<=m[1].to_i}}
