good = r'''
           /|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
'''
bad = r'''
888                          888      
888                          888      
888                          888      
888888 .d88b. 888d888 .d8888b88888b.  
888   d88""88b888P"  d88P"   888 "88b 
888   888  888888    888     888  888 
Y88b. Y88..88P888    Y88b.   888  888 
 "Y888 "Y88P" 888     "Y8888P888  888 
'''


torch_lit = True
if torch_lit:
    outcome = "Flicker: The torch provides light."
    print(good)
else:
    outcome = "Doom: You have no light and die."
    print(bad)
print(outcome)

