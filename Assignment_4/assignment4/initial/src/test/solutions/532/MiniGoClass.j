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
	astore_1
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_5
	putfield A/x I
	dup
	ldc 10.0
	putfield A/y F
	astore_1
	aload_1
	invokevirtual A/foo()I
	invokestatic io/putIntLn(I)V
.var 2 is b LB; from Label2 to Label3
	aload_1
	astore_2
	aload_2
	invokeinterface B/foo()I 1
	invokestatic io/putIntLn(I)V
.var 3 is c LB; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	dup
	bipush 10
	putfield A/x I
	dup
	ldc 20.0
	putfield A/y F
	astore_3
	aload_3
	invokeinterface B/foo()I 1
	invokestatic io/putIntLn(I)V
.var 4 is d LB; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	dup
	bipush 10
	putfield A/x I
	dup
	ldc 8.5
	putfield A/y F
	astore 4
	aload 4
	invokeinterface B/foo()I 1
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 5
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
