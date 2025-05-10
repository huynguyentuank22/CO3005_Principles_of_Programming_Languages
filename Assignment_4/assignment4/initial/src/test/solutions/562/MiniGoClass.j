.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is temp LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_1
	putfield A/x I
	dup
	ldc 0.0
	putfield A/y F
	dup
	iconst_0
	putfield A/z Z
	dup
	new String_MiniGo
	dup
	ldc ""
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield A/s LString_MiniGo;
	astore_1
	aload_1
	invokevirtual A/print()V
.var 2 is temp1 LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_0
	putfield A/x I
	dup
	ldc 2.0
	putfield A/y F
	dup
	iconst_0
	putfield A/z Z
	dup
	new String_MiniGo
	dup
	ldc ""
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield A/s LString_MiniGo;
	astore_2
	aload_2
	invokevirtual A/print()V
.var 3 is temp2 LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_0
	putfield A/x I
	dup
	ldc 0.0
	putfield A/y F
	dup
	iconst_1
	putfield A/z Z
	dup
	new String_MiniGo
	dup
	ldc ""
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield A/s LString_MiniGo;
	astore_3
	aload_3
	invokevirtual A/print()V
.var 4 is temp3 LA; from Label2 to Label3
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_0
	putfield A/x I
	dup
	ldc 0.0
	putfield A/y F
	dup
	iconst_0
	putfield A/z Z
	dup
	new String_MiniGo
	dup
	ldc "abc"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putfield A/s LString_MiniGo;
	astore 4
	aload 4
	invokevirtual A/print()V
Label3:
Label1:
	return
.limit stack 9
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
