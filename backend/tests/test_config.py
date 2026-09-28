from __future__ import annotations

import unittest

from app import config


class LocalEnvironmentOverrideTests(unittest.TestCase):
    def setUp(self) -> None:
        self.local_env_path = config.BASE_DIR / '.env.local'
        self.original_content = self.local_env_path.read_text(encoding='utf-8') if self.local_env_path.exists() else None
        self.local_env_path.write_text(
            'POSTGRES_DSN=postgresql://local:local@127.0.0.1:5432/local_test\n',
            encoding='utf-8',
        )
        config.get_settings.cache_clear()

    def tearDown(self) -> None:
        if self.original_content is None:
            self.local_env_path.unlink(missing_ok=True)
        else:
            self.local_env_path.write_text(self.original_content, encoding='utf-8')
        config.get_settings.cache_clear()

    def test_local_environment_file_overrides_template_database_dsn(self) -> None:
        settings = config.get_settings()

        self.assertEqual(settings.postgres_dsn, 'postgresql://local:local@127.0.0.1:5432/local_test')
