.source Vehicle.java
.class public Vehicle
.super java.lang.Object
.field public model Ljava/lang/String;
.field public mfg_year I

.method public <init>(Ljava/lang/String;I)V
Label0:
.var 0 is this LVehicle; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is model Ljava/lang/String; from Label0 to Label1
.var 2 is mfg_year I from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Vehicle/model Ljava/lang/String;
	aload_0
	iload_2
	putfield Vehicle/mfg_year I
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LVehicle; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public display()V
Label0:
.var 0 is this LVehicle; from Label0 to Label1
Label2:
	ldc "Model: "
	aload_0
	getfield Vehicle/model Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Vehicle/mfg_year I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public updateModel(Ljava/lang/String;)V
Label0:
.var 0 is this LVehicle; from Label0 to Label1
.var 1 is new_model Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Vehicle/model Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
