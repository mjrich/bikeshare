library("foreign")
library("Deducer")
library("Hmisc")
library("doBy")



setwd("~/dev/bikeshare")


data = read.csv("2011-combined.csv", header=T, sep=",")

head(data)
        
frequencies(data$Member.Type)

frequencies(data$Bike.)

frequencies(data$Start.station)
frequencies(data$End.station)


biketable = table(data$Bike.)
biketable[order(biketable, decreasing=T)][1:10]

durationtable = table(data$Duration)
durationtable[order(durationtable, decreasing=F)][1:500]


data["startTime"] = NA
data$startTime = strptime(data$Start.date, "%m/%d/%Y %H:%M")
summary(data$startTime)

data["EndTime"] = NA
data$EndTime = strptime(data$End.date, "%m/%d/%Y %H:%M")
summary(data$EndTime)

data["tripTime"] = NA
data$tripTime = (data$EndTime - data$startTime)
summary(data$tripTime)

describe(data$tripTime)

median(data$tripTime)
mean(data$tripTime)
mode(data$tripTime)


data["trip.Combined"] = NA
data$trip.Combined = (paste(data$Start.station, "-", data$End.station))
CombinedTriptable = table(data$trip.Combined)
CombinedTriptable[order(CombinedTriptable, decreasing=T)][1:10]


sumtable = summaryBy(tripTime + Member.Type ~ trip.Combined, data = data, 
    FUN = function(x) { c(mu = mean(x), md = median(x), s = sd(x), n = length(x)) }, order=FALSE )
# produces tripTime.mu tripTime.md tripTime.s for each level of trip.Combined

sumtable[order(sumtable$tripTime.n, decreasing=T),c(1,2,3,4,5)][c(0:20),]

write.table(sumtable, "BikeTripDuration.txt", sep="\t")




