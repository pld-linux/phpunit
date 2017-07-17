<?php
/* Autoloader for phpunit/phpunit and its dependencies */

/* Required */
require_once 'File/Iterator/Autoload.php';
require_once 'PHP/CodeCoverage/Autoload.php';
require_once 'PHP/Timer/Autoload.php';
require_once 'PHPUnit/Framework/MockObject/Autoload.php';
require_once 'Text/Template/Autoload.php';
require_once 'PHP/Invoker/Autoload.php';
require_once 'SebastianBergmann/Diff/autoload.php';
require_once 'SebastianBergmann/Environment/autoload.php';
require_once 'SebastianBergmann/Exporter/autoload.php';
require_once 'SebastianBergmann/Version/autoload.php';
require_once 'SebastianBergmann/Comparator/autoload.php';
require_once 'SebastianBergmann/GlobalState/autoload.php';
require_once 'Doctrine/Instantiator/autoload.php';
require_once 'Prophecy/autoload.php';

$vendorDir = stream_resolve_include_path('Symfony/Component/ClassLoader/ClassLoader.php');
$vendorDir = dirname(dirname(dirname(dirname($vendorDir))));
// Use Symfony autoloader
if (!isset($classLoader) || !($classLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once $vendorDir . '/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $classLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $classLoader->register();
}

/* for symfony/yaml */
$classLoader->addPrefix('Symfony\\Component\\', $vendorDir);

spl_autoload_register(
  function ($class)
  {
      static $classes = NULL;

      if ($classes === NULL) {
          $classes = array(
            ___CLASSLIST___
          );
      }

      $cn = strtolower($class);

      if (isset($classes[$cn])) {
          require __DIR__ . $classes[$cn];
      }
  }
);

/* Optional */
foreach(array(
            'PHPUnit/Extensions/Database/Autoload.php',
            'PHPUnit/Extensions/SeleniumCommon/Autoload.php',
            'PHPUnit/Extensions/SeleniumTestCase/Autoload.php',
            'PHPUnit/Extensions/Story/Autoload.php'
        ) as $opt) {
    if ($fic = stream_resolve_include_path($opt)) {
        require_once $fic;
    }
}
