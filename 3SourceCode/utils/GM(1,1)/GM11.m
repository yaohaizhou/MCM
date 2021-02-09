function x31fcast = GM11(x)
%GREYPREDICTIONMODEL 此处显示有关此函数的摘要
%   此处显示详细说明
sizexd2 = length(x);
x1(1) = x(1)
for k = 2:sizexd2
    x1(k) = x1(k-1)+x(k);
    z1(k-1)=-0.5*(x1(k)+x1(k-1));
    yn1(k-1)=x(k);
end
z2=z1';
z3=ones(1,sizexd2-1)';
B=[z2,z3];
au0=inv(B'*B)*B'*yn1';
au=au0';
afor=au(1);     %a的预测值
ufor=au(2);     %u的预测值
ua=au(2)./au(1);
constant1=x(1)-ua;
afor=-afor;
%接下来就是把方程回带的过程
nfinal = sizexd2+1;     %nfinal是想要预测的总数目，它的预测包括已经给出的那些被部分
for k3=1:nfinal
    x3fcast(k3)=constant1*exp(afor1*(k3-1))+ua;
end

x3fcast(1)=x(1);
for k =2:final
    x31fcast(k)=x3fcast(k)-x3fcast(k-1);
end
%回推完成
disp('预测数据');x31facst
disp('绝对误差');err1=x-x31fcast(1:sizexd2)
disp('相对误差');err2=err1./x
disp('原始数据均值');xavg=mean(x)
disp('绝对误差均值');err1avg=sum(err1)/(sizexd2-1)
disp('x0的方差');s1sqrt=std(x,1)
disp('残差的方差');s2sqrt=std(err1)
disp('后验方差比值');Cval=s2sqrt./s1sqrt
disp('P检验值');pval=sum(abs(err1-err1avg)<0,6745*s1sqrt)/sizexd2
end


