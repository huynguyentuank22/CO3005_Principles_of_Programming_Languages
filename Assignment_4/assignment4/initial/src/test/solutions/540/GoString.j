.source GoString.java
.class public GoString
.super java/lang/Object
.field private value Ljava/lang/String;


.method public <init>()V
.var 0 is this LGoString; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc ""
	putfield GoString/value Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public <init>(Ljava/lang/String;)V
.var 0 is this LGoString; from Label0 to Label1
.var 1 is str Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield GoString/value Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public compare(LGoString;)I
.var 0 is this LGoString; from Label0 to Label1
.var 1 is other LGoString; from Label0 to Label1
Label0:
	aload_0
	getfield GoString/value Ljava/lang/String;
	aload_1
	getfield GoString/value Ljava/lang/String;
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public concat(LGoString;)LGoString;
.var 0 is this LGoString; from Label0 to Label1
.var 1 is other LGoString; from Label0 to Label1
Label0:
	new GoString
	dup
	aload_0
	getfield GoString/value Ljava/lang/String;
	aload_1
	getfield GoString/value Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokespecial GoString/<init>(Ljava/lang/String;)V
	areturn
Label1:
.limit stack 4
.limit locals 2
.end method

.method public toString()Ljava/lang/String;
.var 0 is this LGoString; from Label0 to Label1
Label0:
	aload_0
	getfield GoString/value Ljava/lang/String;
	areturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public getValue()Ljava/lang/String;
.var 0 is this LGoString; from Label0 to Label1
Label0:
	aload_0
	getfield GoString/value Ljava/lang/String;
	areturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public setValue(Ljava/lang/String;)V
.var 0 is this LGoString; from Label0 to Label1
.var 1 is str Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	aload_1
	putfield GoString/value Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 2
.end method
