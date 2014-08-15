# -*- coding: utf-8 -*-
"""
Simple timer for profiling code execution time

@author: Roger Woodman
"""

import datetime
import time

class ExecutionTimer():
    """Simple timer class for profiling code execution time"""
    
    def __init__(self, verboseOutput = False):
        """Starts execution timer
        
        :param verboseOutput: If true, execution time output will be more descriptive
        """
        self.verboseOutput = verboseOutput
        self.timeStart = self.resetTimer()
        self.timeEnd = -1
        self.executionDuration = -1
    
    def resetTimer(self):
        """Captures the current time as the start time"""
        self.timeStart = datetime.datetime.now()
        return self.timeStart        
        
    def stopTimer(self, printToScreen = True):
        """Stops timer
        
        :param printToScreen: Print execution time to the screen
        """
        # Calculate excecution duration
        self.timeEnd = datetime.datetime.now()
        self.executionDuration = self.timeEnd - self.timeStart
        # Print the execution duration to the screen
        if(printToScreen):
            self.printExecutionTime()
        return self.executionDuration

    def getStartTime(self):
        """Get start time"""
        return self.timeStart

    def getEndTime(self):
        """Get end time"""
        return self.timeEnd
        
    def getExecutionDuration(self):
        """Get execution duration"""
        return self.executionDuration
        
    def printExecutionTime(self):
        """Prints execution time"""
        if(self.verboseOutput):
            print("Execution time: %s second(s) %s ms" % (self.executionDuration.seconds, self.executionDuration.microseconds / 1000))           
        else:
            print("Execution time: %s" % self.executionDuration)    
    
if __name__ == '__main__':
    # Execution timer test
    executionTimer = ExecutionTimer(verboseOutput = True)
    time.sleep(42.42)
    executionTimer.stopTimer()