import warnings

class DefaultConfig(object):

    env = 'default'

    dic_ce_path = './dic/stardict-langdao-ce-big5-2.4.2'
    dic_ec_path = './dic/stardict-langdao-ec-big5-2.4.2'

def parse(self, kwargs):

    for k, v in kwargs.iteritems():
        if(not hasattr(self, k)):
            warnings.warn('Warning: opt has not attribute %s' % k)
        setattr(self, k, v)

    print('user config:')
    for k, v in self.__class__.__dict__.iteritems():
        if not k.startswith('__'):
            print(k, getattr(self, k))

DefaultConfig.parse = parse
opt = DefaultConfig()