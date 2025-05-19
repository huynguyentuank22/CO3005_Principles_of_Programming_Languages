.source User.java
.class public User
.super java.lang.Object
.field public id Ljava/lang/String;
.field public score I
.field public rating F
.field public vehicle LVehicle;

.method public <init>(Ljava/lang/String;IFLVehicle;)V
Label0:
.var 0 is this LUser; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is id Ljava/lang/String; from Label0 to Label1
.var 2 is score I from Label0 to Label1
.var 3 is rating F from Label0 to Label1
.var 4 is vehicle LVehicle; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield User/id Ljava/lang/String;
	aload_0
	iload_2
	putfield User/score I
	aload_0
	fload_3
	putfield User/rating F
	aload_0
	aload 4
	putfield User/vehicle LVehicle;
Label3:
Label1:
	return
.limit stack 6
.limit locals 5
.end method

.method public <init>()V
Label0:
.var 0 is this LUser; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public showDetails()V
Label0:
.var 0 is this LUser; from Label0 to Label1
Label2:
	ldc "User ID: "
	aload_0
	getfield User/id Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield User/score I
	invokestatic io/putIntLn(I)V
	aload_0
	getfield User/rating F
	invokestatic io/putFloatLn(F)V
	aload_0
	getfield User/vehicle LVehicle;
	invokevirtual Vehicle/display()V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
