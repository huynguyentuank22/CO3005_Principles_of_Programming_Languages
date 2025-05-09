.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

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
	aload_1
	invokevirtual A/foo()LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual A/setS(LGoString;)V
	aload_1
	invokevirtual A/getS()LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
.var 2 is b LB; from Label2 to Label3
	aload_1
	astore_2
	aload_2
	new GoString
	dup
	ldc "aaa"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokeinterface B/setS(LGoString;)V 2
	aload_2
	invokeinterface B/getS()LGoString; 1
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 5
.limit locals 3
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
