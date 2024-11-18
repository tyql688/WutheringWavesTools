class WavesException(Exception):
    def __init__(self, errorCode, message):
        super(WavesException, self).__init__(errorCode, message)

    @property
    def errorCode(self):
        return self.args[0]

    @property
    def message(self):
        return self.args[1]

    def __str__(self):
        return '%s:%s' % (self.errorCode, self.message)

    def __unicode__(self):
        return u'%s:%s' % (self.errorCode, self.message)


class WavesRegister(object):
    _id_cls_map = {}

    @classmethod
    def find_class(cls, _id):
        return cls._id_cls_map.get(_id)

    @classmethod
    def register_class(cls, _id, _clz):
        old_cls = cls.find_class(_id)
        if old_cls:
            raise TypeError('%s already register %s for type %s' % (cls, old_cls, _id))
        cls._id_cls_map[_id] = _clz


class WavesWeaponRegister(WavesRegister):
    pass


class WavesEchoRegister(WavesRegister):
    pass


class WavesCharRegister(WavesRegister):
    pass
