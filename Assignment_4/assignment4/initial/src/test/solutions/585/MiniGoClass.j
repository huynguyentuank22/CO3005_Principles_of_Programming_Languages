.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static test(LGoString;LA;LB;)V
.var 0 is x LGoString; from Label0 to Label1
.var 1 is a LA; from Label0 to Label1
.var 2 is b LB; from Label0 to Label1
Label0:
Label2:
	aload_0
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokevirtual GoString/setValue(Ljava/lang/String;)V
	aload_1
	new GoString
	dup
	ldc "World"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual A/setS(LGoString;)V
	aload_2
	new GoString
	dup
	ldc "!"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokeinterface B/setS(LGoString;)V 2
Label3:
Label1:
	return
.limit stack 7
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	dup
	new GoString
	dup
	ldc ""
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putfield A/s LGoString;
	astore_1
.var 2 is b LB; from Label2 to Label3
	aload_1
	astore_2
.var 3 is c LGoString; from Label2 to Label3
	new GoString
	dup
	ldc ""
	invokespecial GoString/<init>(Ljava/lang/String;)V
	astore_3
	aload_3
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	invokevirtual A/getS()LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_2
	invokeinterface B/getS()LGoString; 1
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_3
	aload_1
	aload_2
	invokestatic MiniGoClass/test(LGoString;LA;LB;)V
	aload_3
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	invokevirtual A/getS()LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_2
	invokeinterface B/getS()LGoString; 1
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 5
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label4:
Label5:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
