# rcdumper
RepChain转储小工具，为数据标准验证创建的试验性项目。

RepChain版本：https://gitee.com/BTAJL/repchain/commit/add8cefecb76a92e3b814872ce8dd520a236bb5d

`demo_data_standard.py`提交一个签名交易到RepChain，调用智能合约计算转账合约账户状态的sha256。需要python版SDK——RCPython的支持。

`fetch_and_compare.py`提供了反序列化和通过HTTP请求访问RepChain区块数据的方法。

`dumper.py`将RepChain的leveldb底层文件复制一份到当前目录下的lvldb中，能够：

- 将转账合约账户状态导出成JSON，实现转储
- 利用leveldb底层文件，链下计算转账合约账户状态的sha256
- 从RepChain区块数据中解析得到智能合约计算的sha256，和本地计算的进行对比





