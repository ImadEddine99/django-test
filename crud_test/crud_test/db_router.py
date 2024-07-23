class DatabaseRouter_test_1:
    def db_for_read(self, model, **hints):
        # return getattr(model._state, 'db', 'test_1')
        return 'test_1'

    def db_for_write(self, model, **hints):
        return 'test_1'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'test_1'
    
class DatabaseRouter_test_2:
    def db_for_read(self, model, **hints):
        return 'test_2'

    def db_for_write(self, model, **hints):
        return 'test_2'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'test_2'
    
class DatabaseRouter_test_3:
    def db_for_read(self, model, **hints):
        return 'test_3'

    def db_for_write(self, model, **hints):
        return 'test_3'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'test_3'