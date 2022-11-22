<?xml version="1.0"?>
<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:html="http://www.w3.org/1999/xhtml"
    xmlns="http://www.w3.org/1999/xhtml">

<xsl:template match="/Journalists">
<html>
    <head>
        <link href="vanilla.css" rel="stylesheet" crossorigin="anonymous" />
    </head>
    <body>
        <h1>Journalists on Mastodon</h1>
        <h2>
            About this website
        </h2>
        <blockquote style="background-color: #fbecb5;">
            Data collected by <a href="https://indieweb.social/@tchambers">Tim Chambers</a> and made available
            <a href="https://docs.google.com/spreadsheets/d/13No4yxY-oFrN8PigC2jBWXreFCHWwVRTftwP6HcREtA/edit?resourcekey=undefined#gid=1320898902">
            here</a>. Exported on Nov 22 08:45 CET. This website was created by <a href="https://infosec.exchange/@ndurner">Nils Durner</a>. Personal use only. Any and all warranties and guarantees disclaimed.
            Please <a href="https://github.com/ndurner/journalists_on_mastodon/issues">report issues here</a> or get in touch on Mastodon.
        </blockquote>
        <xsl:apply-templates />
    </body>
</html>
</xsl:template>

<xsl:template match="Journalist">
    <article>
        <header>
            <h1>
                <xsl:value-of select="Name" />
            </h1>
        </header>
        <p>
            Mastodon:
            <xsl:choose>
                <xsl:when test="string-length(Link) > 0">
                    <a>
                        <xsl:attribute name="href">
                            <xsl:value-of select="Link" />
                        </xsl:attribute>
                        <xsl:value-of select="Mastodon" />
                    </a>        
                </xsl:when>
                <xsl:otherwise>
                    <xsl:value-of select="Mastodon" />
                </xsl:otherwise>
            </xsl:choose>
            | Twitter:
            <a>
                <xsl:attribute name="href">
                    <xsl:value-of select="concat('https://twitter.com/', Twitter)" />
                </xsl:attribute>
                <xsl:value-of select="Twitter" />
            </a>
        </p>

        <blockquote>
                <p>
                    <b>Main areas: </b>
                    <xsl:value-of select="Main" />
                </p>
                <xsl:if test="string-length(Outlets/text()) > 0">
                    <p>
                        <b>Outlets: </b>
                        <xsl:value-of select="Outlets" />
                    </p>    
                </xsl:if>
                <xsl:if test="string-length(Other/text()) > 0">
                    <p>
                        <b>Other info: </b>
                        <xsl:value-of select="Other" />
                    </p>        
                </xsl:if>
        </blockquote>
    </article>
</xsl:template>

</xsl:stylesheet>