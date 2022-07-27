class Electronic():
    processor = '8 gb octacore'
    ram = '8 gb'      
    properties = ['bluetooth'  ,'speaker'  ,'wifi' ]
    def testproperties(self ) :
       if self.properties [bluetooth] == True: 
         print("bluetooth is working")
       else :       
          print("bluetooth is not working")
obj = Electronic()                    
test = obj.testproperties()
