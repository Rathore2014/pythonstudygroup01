class electronic:
    def __init__(self):
        self.cpu_cores = 8
        self.memory_gb = 8
        self.support_feature =('wifi','bluetuth','speaker')
    def feature_support(self,feature_name):    
        for i in range(len(self.support_feature)-1):
            if feature_name == self.support_feature[i]:
                return True
        return False 
    def printingsupportfeature(self):
        count = 0 
        for feature in self.support_feature:
           count += 1
        print(f"feature {count} is {feature} (count.feature)")
obj=electronic()
obj.printingsupportfeature()       