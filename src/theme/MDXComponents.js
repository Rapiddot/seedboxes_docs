import React from 'react';
// Importing the original mapper + our components according to the Docusaurus doc
import MDXComponents from '@theme-original/MDXComponents';
import Button from '@site/src/components/Button';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'; // Import the FontAwesomeIcon component.
import { library } from '@fortawesome/fontawesome-svg-core'; // Import the library component.
import { fab } from '@fortawesome/free-brands-svg-icons'; // Import all brands icons.
import { fas } from '@fortawesome/free-solid-svg-icons'; // Import all solid icons.

library.add(fab, fas); // Add all icons to the library so you can use them without importing them individually.

export default {
  // Reusing the default mapping
  ...MDXComponents,
  Button,
  FAIcon: FontAwesomeIcon,
};