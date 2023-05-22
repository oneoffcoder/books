#Import dataset (code below only works if file is in working directory)
med <- read.csv('MedicalData.csv')

#Confirm normality assumption
boxplot(med$BP~med$Age,main='Blood Pressure by Age Group',ylab='Blood Pressure (mmHg)')
boxplot(med$BP~med$Edema,main='Blood Pressure by Edema Status',ylab='Blood Pressure (mmHg)')

#Define "Edema" as a factor (categorical) variable
med$Edema <- as.factor(med$Edema)

#Confirm equal variance assumption
install.packages(car)
library(car)
leveneTest(med$BP~med$Age)
leveneTest(med$BP~med$Edema)

#Build Two-way ANOVA model with interaction and view results
my2aov <- aov(BP~Age*Edema, data=med, contrasts=list(Age=contr.sum, Edema=contr.sum))
Anova(my2aov, type=3)

#Calculate R-squared
summary.lm(my2aov)$adj.r.squared

#Pairwise comparisons with Tukey adjustment
TukeyHSD(my2aov)
