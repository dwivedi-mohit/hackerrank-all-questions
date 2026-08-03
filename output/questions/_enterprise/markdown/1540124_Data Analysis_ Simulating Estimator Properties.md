# Data Analysis: Simulating Estimator Properties

## Metadata

- **ID:** 1540124
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Data Analysis, Abstraction, R, Easy
- **Skills:** R (Basic)

## Summary

This multiple choice question evaluates OLS regression, simulation in R, and statistical analysis concepts, ideal for junior-level roles. The problem requires understanding the output of R code that simulates data and fits a regression model to analyze relationships between variables.

## Problem Statement

`set.seed(5872)

reps<-1000
b0<-0.2
b1<-0.5
b2<-0.75
n<-1000
cor.level<-c(seq(0,0.99,0.1),0.99)
par.est.ov<-matrix(NA,nrow=reps,ncol=length(cor.level))
mse.ov<-matrix(NA,nrow=length(cor.level),ncol=1)

for(j in 1:length(cor.level)){

	for(i in 1:reps){

		X.corr<-matrix(c(1,cor.level[j],cor.level[j],1),nrow=2,ncol=2)
		X<-rmvnorm(n,mean=c(0,0),sigma=X.corr)
		X1<-X[,1]
		X2<-X[,2]
		Y<-b0+b1*X1+b2*X2+rnorm(n,mean=0,sd=1)
		model<-lm(Y~X1)
		par.est.ov[i,j]<-model$coef[2]

		}

	mse.ov[j]<-mean((par.est.ov[,j]-b1)^2)

	cat("Completed cor =",cor.level[j], "\n")

	}

plot(density(par.est.ov[,1]),xlim=c(0.2,1.6),ylim=c(0,15),lwd=3,
xlab=expression(hat(beta)[1]),ylab="Density",main=expression(paste("Distribution of ",
hat(beta)[1])))
	lines(density(par.est.ov[,11]),lwd=3,lty="dashed")
	abline(v=b1)
	text(0.67,12,expression(paste("True ", beta[1]==0.5)),cex=1)
	legend("topright",
	legend=c(expression(r[x[1]][x[2]] == 0),expression(r[x[1]][x[2]] == 0.99))[c(1,2)],
	col=c("black","black")[c(1,2)],lwd=c(3,3),lty=c(1,2)[c(1,2)],bg="white")`
```

Which statement correctly describes the R code?

## Preview

set.seed(5872)
