.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a LString_MiniGo;
.field static b LB;
.field static c LC;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/a LString_MiniGo;
	getstatic MiniGoClass/b LB;
	getstatic MiniGoClass/c LC;
	invokestatic MiniGoClass/testPassByRef(LString_MiniGo;LB;LC;)V
	getstatic MiniGoClass/a LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MiniGoClass/b LB;
	invokevirtual B/getA()I
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/c LC;
	invokeinterface C/getA()I 1
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static testPassByRef(LString_MiniGo;LB;LC;)V
.var 0 is s LString_MiniGo; from Label0 to Label1
.var 1 is m LB; from Label0 to Label1
.var 2 is n LC; from Label0 to Label1
Label0:
Label2:
	aload_0
	new String_MiniGo
	dup
	ldc "hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokevirtual String_MiniGo/setValue(Ljava/lang/String;)V
	aload_1
	invokevirtual B/foo()V
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
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/a LString_MiniGo;
	new B
	dup
	invokespecial B/<init>()V
	dup
	iconst_5
	putfield B/a I
	dup
	ldc 10.0
	putfield B/b F
	putstatic MiniGoClass/b LB;
	getstatic MiniGoClass/b LB;
	putstatic MiniGoClass/c LC;
Label0:
Label1:
	return
.limit stack 4
.limit locals 0
.end method
