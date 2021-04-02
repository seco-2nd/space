#Import dataset & test
hospital <- read.csv(file.choose())
hospital

#Q1
hist(hospital$AGE,main="Frequency of patients",ylab="Visits",xlab="Age") 
max1<-summary(as.factor(hospital$AGE))
head(sort(max1, decreasing = TRUE),1)
max2<-aggregate(TOTCHG~AGE,sum,data = hospital)
head(max2[order(-max2$TOTCHG),],1)

#Q2
hist(hospital$APRDRG,main="Frequency of Treatments",ylab="Visits",xlab="Groups")
max1<-summary(as.factor(hospital$APRDRG))
head(sort(max1, decreasing = TRUE),1)
max2<-aggregate(TOTCHG~APRDRG,sum,data=hospital)
head(max2[order(-max2$TOTCHG),],1)

#Q3
hosp<-na.omit(hospital)
aov(TOTCHG~RACE,data = hosp)
summary(aov(TOTCHG~RACE,data = hosp))
summary(as.factor(hosp$RACE))

#Q4
summary(lm(TOTCHG~AGE+FEMALE,data = hosp))
summary(as.factor(hosp$FEMALE))

#Q5
summary(lm(LOS~AGE+FEMALE+RACE,data=hosp))

#Q6
summary(lm(TOTCHG~AGE+FEMALE+RACE+LOS+APRDRG,data = hosp))