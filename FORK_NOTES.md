# MCP runtime fork

This branch supports the `west-control` MCP project.

The default dependency set contains only packages imported by the login,
state-inspection, work-list, and job-queue paths. Notebook, plotting, database,
and additional validation packages remain available through Poetry's optional
`extended` dependency group.

The fork does not change login endpoints or add game actions. It fixes
`work_task` payload construction so task fields are plain strings and
multi-task requests use successive queue positions. Safety policy, mission
validation, free-account queue limits, premium restrictions, compact results,
and Chrome verification live in the separate MCP wrapper.
