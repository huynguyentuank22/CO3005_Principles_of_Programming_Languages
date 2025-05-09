.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a I from Label2 to Label3
	iconst_5
	istore_1
.var 2 is b I from Label2 to Label3
	iconst_0
	istore_2
	iload_2
	iconst_0
	if_icmpeq Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	dup
	ifle Label4
	pop
	iload_1
	iload_2
	idiv
	iconst_2
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
Label4:
	ifle Label9
Label11:
Label12:
	new GoString
	dup
	ldc "Division result > 2"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label13:
	goto Label10
Label9:
Label14:
Label15:
	new GoString
	dup
	ldc "Safe from division by zero"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label16:
Label10:
	iconst_2
	istore_2
	iload_2
	iconst_0
	if_icmpeq Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	dup
	ifle Label17
	pop
	iload_1
	iload_2
	idiv
	iconst_2
	if_icmple Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
Label17:
	ifle Label22
Label24:
Label25:
	new GoString
	dup
	ldc "Division result > 2"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label26:
	goto Label23
Label22:
Label27:
Label28:
	new GoString
	dup
	ldc "Division result <= 2"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label29:
Label23:
Label3:
Label1:
	return
.limit stack 19
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label30:
Label31:
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
