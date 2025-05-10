.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static concatenate(LString_MiniGo;LString_MiniGo;)LString_MiniGo;
.var 0 is s1 LString_MiniGo; from Label0 to Label1
.var 1 is s2 LString_MiniGo; from Label0 to Label1
Label0:
Label2:
.var 2 is result LString_MiniGo; from Label2 to Label3
	aload_0
	astore_2
Label6:
.var 3 is i I from Label6 to Label7
	iconst_0
	istore_3
Label8:
	iload_3
	iconst_2
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label5
	goto Label9
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label8
Label9:
Label12:
	aload_2
	aload_2
	aload_1
	invokevirtual String_MiniGo/concat(LString_MiniGo;)LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokevirtual String_MiniGo/setValue(Ljava/lang/String;)V
Label13:
	goto Label4
Label5:
Label7:
	aload_2
	areturn
Label3:
Label1:
.limit stack 10
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is str LString_MiniGo; from Label2 to Label3
	new String_MiniGo
	dup
	ldc "Hi"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	new String_MiniGo
	dup
	ldc "!"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokestatic MiniGoClass/concatenate(LString_MiniGo;LString_MiniGo;)LString_MiniGo;
	astore_1
	aload_1
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
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
