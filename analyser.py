"""Analyser class for running analsis on columns"""

import re
from collections import Counter
from statistics import mean, mode, median_low, median, median_high, stdev, \
    StatisticsError, Decimal
from scipy.stats import mstats
from numpy import array
from email.utils import parseaddr
from math import floor, log10, pow



#  Config
threshold = 0.9
enum_threshold = 1
standardDeviations = 3

class Analyser(object):
    """Base analysis class object. Initiate the object, and assigns the 
    statistical mode, if any.
    
    Class variables:
    mode -- Returns the mode of the column analysed.
    
    Child Classes and associated variables:
    StringAnalyser -- String column analysis.
    EmailAnalyser -- Email column analysis.
    EnumAnalyser -- Enumerated column analysis.
    NumericalAnalyser -- String/Float column analysis.
        min -- Minimum value in column values.
        max -- Maximum value in column values.
        mean -- Mean value in column values.
        median_low -- Low median for column values.
        median -- Median value for column values.
        median_high -- High median for column values.
        normDist -- String Yes/No if columns value is normally distributed.
        stdev -- Standard deviation for column values, N/A if not normally distributed to
                    to within 95.5% confidence.
        stDevOutliers -- List of values outside a certain number of standard deviations
                        from the mean.
    CurrencyAnalyser -- Child class of NumericalAnalyser
    BooleanAnalyser -- Boolean column analysis
    """
    def uniqueCount(self, values):
        valSet = set()
        for vals in values:
            valSet.add(vals)
        print("Set stuff")
        print(valSet)
        print(len(valSet))
        return len(valSet)

    def __init__(self, values):
        try:
            self.mode = mode(values)
        except StatisticsError:
            print("Statistics error")
            self.mode = 'N/A'
        self.unique = self.uniqueCount(values)

class EmailAnalyser(Analyser):
    "Run email analysis"
    def __init__(self, values):
        super().__init__(values)
        print(self.mode)
        # TODO Something actually useful for emails.
        
class NumericalAnalyser(Analyser):
    """Runs numeric analysis."""
    def __init__(self, values): 
        new_values = []
        for i in values:
            print("Value: ",i)
            if i != '':
                try:
                    new_values.append(eval(i))
                except NameError:
                    print ("NameError:", i, " is not a numeric type")
                    sys.exit(0)
        values = new_values
       # values = [eval(i) for i in values]
        super().__init__(values)
        self.stDevOutliers = []
        if len(values) >= 8:
            self.pval = mstats.normaltest(array(values))[1]
        else:
            self.pval = 100
        self.min = min(values)
        self.max = max(values)
        self.mean = Decimal(mean(values)).quantize(Decimal('.00000'))
        self.median_low = median_low(values)
        self.median = median(values)
        self.median_high = median_high(values)
        self.stdev = Decimal(stdev(values)).quantize(Decimal('.00'))
        self.normDist = 'No'
        if(self.pval < 0.055):
            self.normDist = 'Yes'
        elif self.pval == 100:
            self.normDist = 'N/A'
        if self.normDist != 'No':
            for value in values:
                if value < (self.mean - standardDeviations * self.stdev) or \
                value > (self.mean + standardDeviations * self.stdev):                
                    self.stDevOutliers.append(value)
        
class CurrencyAnalyser(NumericalAnalyser):
    "Run currency analysis, calls NumericalAnalyser as a superclass"
    def __init__(self, values):
        """for x, value in enumerate(self.values):
            try:
                value[x] = eval(self.values[x])
            except SyntaxError:"""
        super().__init__(values)

class StringAnalyser(Analyser):
    """Run string analysis."""
    def __init__(self, values):
        super().__init__(values)
        #  TODO Implement some string exclusive statistics.


class EnumAnalyser(Analyser):
    """Run enumeration analysis."""
    def __init__(self, values):
        super().__init__(values)
        #  TODO Implement some enum exclusive statistics.
                             
class BooleanAnalyser(Analyser):
    "Run email analysis"
    def __init__(self, values):
        super().__init__(values)

class SciNotationAnalyser(Analyser):
    """Run Scientific notation analysis."""
    def __init__(self, values): 
        new_values = []
        for i in values:
            if i != '':
                new_values.append(eval(i))
        values = new_values
       # values = [eval(i) for i in values]
        super().__init__(values)
        self.stDevOutliers = []
        if len(values) >= 8:
            self.pval = mstats.normaltest(array(values))[1]
        else:
            self.pval = 100
        self.min = self.int_to_sci(min(values))
        self.max = self.int_to_sci(max(values))
        self.mean = self.int_to_sci(mean(values))
   
        self.median_low = self.int_to_sci(median_low(values))
        self.median = self.int_to_sci(median(values))
        self.median_high =  self.int_to_sci(median_high(values))
        self.stdev = self.int_to_sci(stdev(values))
        self.normDist = 'No'
        if(self.pval < 0.055):
            self.normDist = 'Yes'
        elif(self.pval == 100):
            self.normDist = 'N/A'
        if self.normDist != 'No':
            for value in values:
                if value < (float(self.mean) - standardDeviations * float(self.stdev)) or \
                value > (float(self.mean) + standardDeviations * float(self.stdev)):               
                    self.stDevOutliers.append(self.int_to_sci(value))

    def int_to_sci(self, value):
        """Converts numbers into a string in scientific notation form"""
        print ("Value: ", value)
        power = floor(log10(abs(value)))
        base = round(value / pow(10, power), 2)
        if power > 0:
            return str(base) + "E+" + str(power)
        else:
            return str(base) + "E" + str(power)
        