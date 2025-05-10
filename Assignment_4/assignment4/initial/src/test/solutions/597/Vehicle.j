.source Vehicle.java
.class public Vehicle
.super java/lang/Object
.implements Transport
.field speed I

.method public <init>()V
.var 0 is this LVehicle; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public getSpeed()I
.var 0 is this LVehicle; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Vehicle/speed I
	ireturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
