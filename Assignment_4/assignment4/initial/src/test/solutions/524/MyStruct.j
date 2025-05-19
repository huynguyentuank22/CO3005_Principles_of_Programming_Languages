.source MyStruct.java
.class public MyStruct
.super java.lang.Object
.implements IfaceA
.implements IfaceB
.field public field_int I
.field public field_float F

.method public <init>(IF)V
Label0:
.var 0 is this LMyStruct; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is field_int I from Label0 to Label1
.var 2 is field_float F from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield MyStruct/field_int I
	aload_0
	fload_2
	putfield MyStruct/field_float F
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LMyStruct; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public getValue()I
Label0:
.var 0 is this LMyStruct; from Label0 to Label1
Label2:
	aload_0
	getfield MyStruct/field_int I
	bipush 100
	iadd
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
