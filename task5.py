good = r'''
                        ad88            
                       d8"              
                       88               
,adPPYba, ,adPPYYba, MM88MMM ,adPPYba,  
I8[    "" ""     `Y8   88   a8P_____88  
 `"Y8ba,  ,adPPPPP88   88   8PP"""""""  
aa    ]8I 88,    ,88   88   "8b,   ,aa  
`"YbbdP"' `"8bbdP"Y8   88    `"Ybbd8"'  
'''
bad = r'''
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
'''


escaped = True
if escaped:
    outcome = "Legend: The drawbridge is raised and you can not make it out."
    print(good)
else:
    outcome = "Doom: You hear the thunder as you make your way outside."
    print(bad)
print(outcome)