#  1..........Electronics: 
#  User Story: As a consumer, I want to be able to organize the tech specs of a Electronics, So that
# I can make more informed decisions when purchasing a Electronics.
#  Acceptance Criteria: Given the Electronics class, When I instantiate a new Electronics
# object, Then the object has the correct properties as described in the assumptions and
# method to test supported features and print all supported features
#  Assumptions: The default Electronics will have 8 cpu cores, 8 GB of memory and
# supports features such as &#39;Wi-Fi&#39;, &#39;Bluetooth&#39;, &#39;Speakers&#39;.
# o Method to test feature which will take input and returns True or False.
# o Method to print all supported features

class Electeronics():
  processor = '8 gb octacore'
  ram = '8 gb'
  properties = {
    'bluethooth':True,
    'speaker':False,
    'wifi':True
  }
  def testProperties(self):
    if self.properties['bluethooth'] == True:
      print('Bluethooth is working')
    else:
      print('Bluethooth is not working')

obj = Electeronics()
test = obj.testProperties()


