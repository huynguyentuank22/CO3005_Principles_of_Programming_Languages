.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a LString_MiniGo;
.field static b LString_MiniGo;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/a LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MiniGoClass/b LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
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
	ldc "ahhaaha"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/a LString_MiniGo;
	new String_MiniGo
	dup
	ldc "hjhjhj"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/b LString_MiniGo;
Label0:
Label1:
	return
.limit stack 3
.limit locals 0
.end method
